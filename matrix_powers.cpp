matrix power(matrix m, long long int n) {
    matrix ret = I;
    for (; n; n >>= 1) {
        if (n & 1) ret *= m;
        m *= m;
    }
    return ret;
}
