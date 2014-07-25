# Usage

    from mongolock import MongoLock

    lock = MongoLock()

    # you can use it as context:
    # (note: if lock is already taken by another worker, MongoLockLocked will raised)
    with lock('key', 'my_worker_name', expires=60, timeout=10):
       # some work here

    # or simply calling methods:
    if lock.lock('key', 'my_worker_name'):
        try:
            # some usefull work
        finally:
            lock.release('key', 'my_worker_name')

    # you can also renew lock by touching it:
    with lock('key', 'my_worker_name', expires=60, timeout=10):
       # some loong loong work here
       lock.touch('key', 'my_worker_name')

Parameters in `lock` method:

  * `key` - name of task to lock
  * `owner` - name of worker, which takes a lock
  * `expire` (optional) - duration in seconds after which lock can be stealed
  * `timeout` (optional) - how long we can wait for a lock (in seconds)

# Configuration nuances

You can configure connection either by specifying connection string,

    lock = MongoLock('localhost:27017')

or by passing configured instance of MongoClient/MongoReplicaSetClient in MongoLock constructor:

    client = MongoClient('localhost:27017')
    lock = MongoLock(client=client)

The second is preferred, as in such a way you can perform more fine grained configuration:

  * use MongoReplicaSetClient
  * specify write concern
  * specify tags
  * etc

# Important things to think about

#### Lock stealing and releasing

You should use unique names for all your workers, if you don't - some strange things may happens.
Consider following sequence:

  * worker1 and worker2 has the same names: worker
  * worker1 achieve lock with expire +30s
  * worker2 try to get lock after 30s (worker1 still working)
  * as lock expires, worker2 steal it
  * now worker1 ends his work and releases lock, as they has same names - lock released
  * worker3 takes a lock, while worker2 still working ...

#### Lock simply not works

If you use cron (or some analogue) to launch tasks on different machines, take in account time drift between machines as well
  as duration of critical section of your tasks.

  * machine1 and machine2 has a time drift 5s
  * worker on machine1 takes a lock on TaskA
  * worker on machine1 done a TaskA in 1s
  * now worker on machine2 comes in play
  * he don't know, that worker on machine1 already complete TaskA
  * he takes a lock on TaskA (without problem as lock was released 4s before) and do it

To prevent such a weird situation, you can simply add some part of time (for example YmdHM) to a key with task name.
