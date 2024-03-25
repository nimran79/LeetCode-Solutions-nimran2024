<h2><a href="https://leetcode.com/problems/dot-product-of-two-sparse-vectors">Dot Product of Two Sparse Vectors</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given two sparse vectors, compute their dot product.</p>

<p>Implement class <code>SparseVector</code>:</p>

<ul>
	<li><code>SparseVector(nums)</code> Initializes the object with the vector <code>nums</code></li>
	<li><code>dotProduct(vec)</code> Compute the dot product between the instance of <code>SparseVector</code> and <code>vec</code></li>
</ul>

<p>A <strong>sparse vector</strong> is a vector that has mostly zero values, you should store the sparse vector <strong>efficiently</strong> and compute the dot product between two <em>SparseVector</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
<strong>Output:</strong> 8
<strong>Explanation:</strong> v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length == nums1.length</code></li>
  <li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 100</code></li>
</ul>

<h2>Solution Notes:</h2>
<p><strong>Time Complexity:</strong> O(n) for creating the tuple of non-zero values; O(L1+L2) for calculating the dot product; where n is the lenth of each array, L1 and L2 are the number of non-zero elements for the two vectors</p>
<p><strong>Space Complexity:</strong> O(L1+L2)</p>

<p><strong>Follow up:</strong> What if only one of the vectors is sparse?</p>
<p><strong>Answer:</strong> Use Binary Search to look for indices from the smaller vector in the bigger vector, and then perform dot product.</p>
