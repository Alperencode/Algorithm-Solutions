/* https://algoleague.com/contest/algorithm-training-beginner-set/problem/ice-cream-yum-yum/detail */
#include <stdio.h>
const int N = 100000;
int a[N];

int main() {
    int n;
    scanf("%d", &n);
    for(int i  = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    // You can calculate your answer now
    // ...
    // Then print your answer to stdout, for example
    // printf("%d", answer);
    
    int min = a[0];
    int sum = 0;
    for(int i  = 0; i < n; i++){
        if(a[i] <= min)
            min = a[i];
        sum += a[i];
    }
            
    sum -= min;
    
    printf("%d", sum);
    
    return 0;
}

// Status: Accepted