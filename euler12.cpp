#include <ctime>
#include <exception>
#include <iostream>
#include <memory>
#include <utility>
#include <vector>
#include <cmath>

using namespace std;

int getTriangularNumber(int term)
{
    int sum = 0;

    for(int i = 1; i < term+1; i++)
    {
        sum += i;
    }

    return sum;
}

int getPrimeFactors(int x)
{
    int count = 0;
    for(int i = 1; i < sqrt(x); i++)
    {
        if(x % i == 0)
        {
            count+=2;
        }
    }
    if(x == sqrt(x)*sqrt(x))
    {
        count--;
    }
    return count;
}

int main()
{
    int term = 2;
    int count = 0;

    while(count < 501)
    {
        cout << "PROCESSING NUMBER: " << getTriangularNumber(term);
        count = getPrimeFactors(getTriangularNumber(term));
        cout << " AT COUNT: " << count << "\n";
        term++;
    }
    return 0;
}