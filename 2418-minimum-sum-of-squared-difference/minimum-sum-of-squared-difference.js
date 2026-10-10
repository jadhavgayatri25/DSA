
var minSumSquareDiff = function(nums1, nums2, k1, k2) {
    let n = nums1.length;
    let k = k1 + k2;
    let diff = new Array(n);
    let maxDiff = 0;
    let total = 0;

    for (let i = 0; i < n; i++) {
        diff[i] = Math.abs(nums1[i] - nums2[i]);
        maxDiff = Math.max(maxDiff, diff[i]);
        total += diff[i];
    }

    if (k >= total) return 0;

    let left = 0, right = maxDiff;

    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        let needed = 0;

        for (let d of diff) {
            if (d > mid) {
                needed += d - mid;
            }
        }

        if (needed <= k) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    let remaining = k;

    for (let i = 0; i < n; i++) {
        if (diff[i] > left) {
            remaining -= diff[i] - left;
            diff[i] = left;
        }
    }

    // Reduce remaining differences by one where possible
    for (let i = 0; i < n && remaining > 0; i++) {
        if (diff[i] === left && left > 0) {
            diff[i]--;
            remaining--;
        }
    }

    let result = 0;

    for (let d of diff) {
        result += d * d;
    }

    return result;
};
