<h2><a href="https://leetcode.com/problems/missing-ranges">Missing Ranges</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>You are given an inclusive range <code>[lower, upper]</code> and a <strong>sorted unique</strong> integer array <code>nums</code>, where all elements are within the inclusive range.
  
A number <code>x</code> is considered missing if <code>x</code> is in the range <code>[lower, upper]</code> and <code>x</code> is not in <code>nums</code>.

Return the <strong>shortest sorted</strong> list of ranges that <strong>exactly covers all the missing numbers</strong>. That is, no element of <code>nums</code> is included in any of the ranges, and each missing number is covered by one of the ranges.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,3,50,75], lower = 0, upper = 99
<strong>Output:</strong> [[2,2],[4,49],[51,74],[76,99]]
<strong>Explanation:</strong> The ranges are:  
  [2,2]
  [4,49]
  [51,74]
  [76,99]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1], lower = -1, upper = -1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no missing ranges since there are no missing numbers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>9</sup> &lt;= lower &lt;= upper &lt;= 10<sup>9</sup></code></li>
  <li><code>0 &lt;= nums.length &lt;= 100</code></li>
  <li><code>lower &lt;= nums[i] &lt;= upper</code></li>
  <li>All the values of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<h2>Solution Notes:</h2>
<p><strong>Time Complexity:</strong> O(n), where n is the length of the array</p>
<p><strong>Space Complexity:</strong> O(1)</p>
