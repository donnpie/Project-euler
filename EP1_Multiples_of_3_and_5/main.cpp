//This programs finds the sum of the multiples of 3 or 5 less than 1000
//eg. the multiples of 3 or 5 below 10 is 3, 5, 6, 9
//the sum of those multiples is 23

#include <iostream>

using namespace std;

    //try 1: brute force
void bruteForce(int three, int five, int max, int &sum) {
    for (int i = 0; i < max; i++) {
        if (i%three == 0 || i%five == 0) {
            sum += i;
        }
    }
//returns: The sum is: 233168
}


int main()
{
    int maxValue = 1000;
    const int THREE = 3;
    const int FIVE = 5;
    int sum = 0;

    bruteForce(THREE, FIVE, maxValue, sum);
    cout << "The sum is: " << sum;

    return 0;
}
