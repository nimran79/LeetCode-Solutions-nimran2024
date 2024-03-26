<h2>Maximum Longest Vacation</a></h2>

You're given a calendar year <code>calendar</code> represented as a char array that contains either <code>H</code> or <code>W</code> where:

H = Holiday W = Workday

Given a number of Personal Time-Off days (PTO), <strong>maximize</strong> the length of the longest vacation you can take.

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<pre>
<strong>Input:</strong> calendar = [W, H, H, W, W, H, W], PTO = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> Your maximum vacation is 5 days.
</pre>


<h2>Solution Notes:</h2>
<p><strong>Time Complexity:</strong> O(n), where n is the number of days in the calendar</p>
<p><strong>Space Complexity:</strong> O(1)</p>
