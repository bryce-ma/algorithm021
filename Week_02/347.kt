class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val frequency = nums.toList().groupingBy { it }.eachCount()
        val pq = PriorityQueue<Pair<Int,Int>>(frequency.size,compareByDescending<Pair<Int, Int>> { it.second })
        frequency.forEach({ pq.add(it.toPair()) })
        val res = (0 until k).map { pq.poll().first }.toIntArray()
        return res
    }
}