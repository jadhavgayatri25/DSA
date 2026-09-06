class Solution {
    public int numDistinct(String s, String t) {
        int n = t.length();

        // dp[j] = number of ways to form first j characters of t
        long[] dp = new long[n + 1];

        // Empty string can be formed in exactly 1 way
        dp[0] = 1;

        for (int i = 0; i < s.length(); i++) {
            // Traverse backwards to avoid overwriting dp[j-1]
            for (int j = n; j >= 1; j--) {
                if (s.charAt(i) == t.charAt(j - 1)) {
                    dp[j] = dp[j] + dp[j - 1];
                }
            }
        }

        return (int) dp[n];
    }
}