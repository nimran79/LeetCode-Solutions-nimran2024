<h2><a href="https://leetcode.com/problems/basic-calculator">Basic Calculator</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>Given a string <code>s</code> representing a valid expression, implement a basic calculator to evaluate it, and return <em>the result of the evaluation</em>.</p>

<p><strong>Note:</strong> You are <strong>not</strong> allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code>eval()</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1 + 1&quot;
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot; 2-1 + 2 &quot;
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(1+(4+5+2)-3)+(6+8)&quot;
<strong>Output:</strong> 23
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of digits, <code>&#39;+&#39;</code>, <code>&#39;-&#39;</code>, <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, and <code>&#39; &#39;</code>.</li>
	<li><code>s</code> represents a valid expression.</li>
	<li><code>&#39;+&#39;</code> is <strong>not</strong> used as a unary operation (i.e., <code>&quot;+1&quot;</code> and <code>&quot;+(2 + 3)&quot;</code> is invalid).</li>
	<li><code>&#39;-&#39;</code> could be used as a unary operation (i.e., <code>&quot;-1&quot;</code> and <code>&quot;-(2 + 3)&quot;</code> is valid).</li>
	<li>There will be no two consecutive operators in the input.</li>
	<li>Every number and running calculation will fit in a signed 32-bit integer.</li>
</ul>

<h2>Solution Notes:</h2>
<p><strong>Time Complexity:</strong> O(n), where n is the length of string</p>
<p><strong>Space Complexity:</strong> O(n), since a stack is used (size up to n).</p>