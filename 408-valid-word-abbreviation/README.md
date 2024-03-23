<h2><a href="https://leetcode.com/problems/valid-word-abbreviation">Valid Word Abbreviation</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>A string can be <strong>abbreviated</strong> by replacing any number of 
  <strong>non-adjacent, non-empty</strong> substrings with their lengths. The lengths <strong>should not</strong> have leading zeros.</p>

For example, a string such as <code>"substitution"</code> could be abbreviated as (but not limited to):

<ul>
	<li><code>"s10n"</code> (<code>"s ubstitutio n"</code>)</li>
	<li><code>"sub4u4"</code> (<code>"sub <u>ubstitutio</u> n"</code>)</li>
  <li><code>"12"</code> (<code>"substitution"</code>)</li>
  <li><code>"su3i1u2on"</code> (<code>"su bst i t u ti on"</code>)</li>
  <li><code>"substitution"</code> (No substrings replaced)</li>
</ul>

The following are <strong>not valid</strong> abbreviations:
- <code>"s10n"</code> (<code>"s ubstitutio n"</code>, the replaced substrings are adjacent)
- <code>"s010n"</code> (has leading zeros)
- <code>"s0ubstitution"</code> (replaces an empty substring)

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = "internationalization", abbr = "i12iz4n"
<strong>Output:</strong> true
<strong>Explanation:</strong> The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = "apple", abbr = "a2e"
<strong>Output:</strong> false
<strong>Explanation:</strong> The word "apple" cannot be abbreviated as "a2e".
</pre>

<h2>Solution Notes:</h2>
<p><strong>Time Complexity:</strong> O(m + n), where m is the length of word and n is the length of abbr</p>
<p><strong>Space Complexity:</strong> O(1)</p>
