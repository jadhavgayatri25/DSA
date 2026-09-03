class Solution {
    public boolean uniformArray(int[] nums1) {
        boolean hasOdd = false;
        boolean hasEven = false;

        for (int x : nums1) {
            if (x % 2 == 0) {
                hasEven = true;
            } else {
                hasOdd = true;
            }
        }

        // All numbers already have the same parity
        if (!hasOdd || !hasEven) {
            return true;
        }

        int min = Integer.MAX_VALUE;

        for (int x : nums1) {
            min = Math.min(min, x);
        }

        // If minimum is odd, every even number
        // can subtract it and become odd.
        if (min % 2 != 0) {
            return true;
        }

        // Minimum is even.
        // An odd number can become even by subtracting
        // another odd number only if a smaller odd exists.
        int minOdd = Integer.MAX_VALUE;

        for (int x : nums1) {
            if (x % 2 != 0) {
                minOdd = Math.min(minOdd, x);
            }
        }

        return minOdd < min;
    }
}