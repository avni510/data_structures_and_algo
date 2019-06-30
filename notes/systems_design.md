#### Systems Design
* Horizontal vs Vertical Scaling
  * vertical scaling - increasing resources for a specific node
  * horizontal scaling - increasing the number of nodes
* Database Denormalization
  * Used to avoid slow joins
  * Adding redundant information to the db to speed up reads
* Database Paritioning (Sharding)
  * Splitting the data across multiple machines 
    * Vertical Partitioning - Paritioning by features
    * Key Based (or Hash Based) partitioning - This uses some part of the data
    to parition it. 
    * Directory Based Partitioning - You maintain a lookup table for where the
    data can be found
* Caching
  * Key Value pairing and typically sits between your application layer
  and your data store
  * The application will first request data from the cache if nothing is found
  it will look up the data in the data store
* Async Processing
  * can sometimes pre process requests through a job queue
  * Ex: re-render part of the web page that has the most popular posts, etc.
* Networking Metrics
  * Bandwidth - The max amount of data tha can be transferred in a unit
  of time. Expressed in bits per second
  * Throughput - the actual amt of data that is transferred
  * Latency - how long it takes data to go from one end to the other
* MapReduce
  * Typically used to process large amts of data
  * write a map step then a reduce step
  * Map
    * takes in data -> emits <key, value>
  * Reduce
    * takes a key and set of associated values -> "reduce" -> <new key, value>

