#include <stdio.h> 

int main(void) {
    int m = 0;
    int n = 0; 
    scanf("%d %d", &m, &n);
    
    if (m < n) {
        int temp = m;
        m = n; 
        n = temp; 
    }
    
    for (int i = n; i > 0; i--) {
        if ((n % i == 0) && (m % i == 0)) {
            printf("%d\n", i); 
            break;
         }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <=  m; j++) {
            if (m * i == n * j) {
                printf("%d\n", m*i); 
                return 0; 
                
             }
         }
    }
}