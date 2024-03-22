<h2><a href="https://leetcode.com/problems/binary-tree-vertical-order-traversal">Binary Tree Vertical Order Traversal</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given the <code>root</code> of a binary tree 
  return <strong>the vertical order traversal</strong> of its nodes' values. (i.e., from top to bottom, column by column).</p>

<p>If two nodes are in the same row and column, the order should be from <strong>left to right</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/vtree1.jpg" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[9],[3,15],[20],[7]]
<strong>Explanation:</strong> Imagine drawing vertical lines through the nodes.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/vtree2-1.jpg" />
<pre>
<strong>Input:</strong> root = [3,9,8,4,0,1,7]
<strong>Output:</strong> [[4],[9],[3,0,1],[8],[7]]
</pre>

<<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/vtree2.jpg" />
<pre>
<strong>Input:</strong> root = [3,9,8,4,0,1,7,null,null,null,2,5]
<strong>Output:</strong> [[4],[9,5],[3,0,1],[8,2],[7]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<h2>Solution Notes:</h2>
<p><strong>Time Complexity:</strong> O(n), where n is the number of nodes in the tree.</p>
<p><strong>Space Complexity:</strong> O(n)</p>
