vector<double> solution(vector<int>& nums, int k) {
    multiset<int> lo, hi;

    vector<double> medians;

    for (int i = 0; i < (int)nums.size(); ++i) {
        int n = nums[i];

        if (i >= k) {
            if (nums[i - k] <= *lo.rbegin()) {
                lo.erase(lo.find(nums[i - k]));
            } else if (!hi.empty()) {
                hi.erase(hi.find(nums[i - k]));
            }
        }

        lo.insert(nums[i]);

        hi.insert(*lo.rbegin());
        lo.erase(prev(lo.end()));

        if (lo.size() < hi.size()) {
            lo.insert(*hi.begin());
            hi.erase(hi.begin());
        }

        if (i >= k - 1) {
            if (k % 2 == 0) {
                medians.push_back(((double)*lo.rbegin() + (double)*hi.begin()) / 2.0);
            } else {
                medians.push_back((double)*lo.rbegin());
            }
        }
    }

    return medians;
}
