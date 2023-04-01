#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b){
    return (*(int*)a - *(int*)b);
}

int main() {
    int n, i, prev, count = 0;
    
    // Inputs
    scanf("%d", &n);
    int arr[n];
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Sort the array
    qsort(arr, n, sizeof(int), compare);

    // Creating prev
    prev = arr[0];
    for(i = 1; i < n; i++){
        // If prev equals or greater than current element
        if(arr[i] <= prev){
            // Increment counter
            count += (prev - arr[i] + 1);
            // Increment prev
            prev = prev + 1;
        }else
            // Assign element to prev
            prev = arr[i];
    }
    printf("%d\n", count);
    return 0;
}
