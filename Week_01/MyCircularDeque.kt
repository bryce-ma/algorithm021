class MyCircularDeque(k: Int) {

    /** Initialize your data structure here. Set the size of the deque to be k. */
    var compacity = k
    var data = IntArray(k)
    var size = 0
    var start = 0
    var end = 0
    private fun nextIndex(i: Int) = (i + 1) % compacity
    private fun previousIndex(i: Int) = (i - 1 + compacity) % compacity


    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    fun insertFront(value: Int): Boolean {
        val notFull = compacity > size
        if (notFull) {
            size ++
            val newStart = previousIndex(start)
            data[newStart] = value
            start = newStart
        }
        return notFull
    }

    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    fun insertLast(value: Int): Boolean {
        val notFull = compacity > size
        if (notFull) {
            this.size ++
            data[end] = value
            end = nextIndex(end)
        }
        return notFull
    }

    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    fun deleteFront(): Boolean {
        val notEmpty = size > 0
        if (notEmpty) {
            this.size --
            start = nextIndex(start)
        }
        return notEmpty
    }

    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    fun deleteLast(): Boolean {
        val notEmpty = !isEmpty()
        if (notEmpty) {
            this.size --
            end = previousIndex(end)
        }
        return notEmpty
    }

    /** Get the front item from the deque. */
    fun getFront(): Int {
        return  if (isEmpty()) -1 else data[start]
    }

    /** Get the last item from the deque. */
    fun getRear(): Int {
        return if (isEmpty()) -1 else data[previousIndex(end)]
    }

    /** Checks whether the circular deque is empty or not. */
    fun isEmpty(): Boolean {
        return size == 0
    }

    /** Checks whether the circular deque is full or not. */
    fun isFull(): Boolean {
        return size == compacity
    }

}


var obj = MyCircularDeque(5)
var param_1 = obj.getFront()
println(param_1)
/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */