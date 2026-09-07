#define MOD 1000000007

int distinctSubseqII(char* s) {
    long long last[26] = {0};
    long long total = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        int idx = s[i] - 'a';

        long long newSubseq = (total + 1) % MOD;

        total = (total + newSubseq - last[idx] + MOD) % MOD;

        last[idx] = newSubseq;
    }

    return (int)total;
}