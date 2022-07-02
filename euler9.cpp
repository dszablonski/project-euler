#include <iostream>
#include <cmath>

using namespace std;

void triple(float a, float b)
{
    float c = sqrt(a*a + b*b);

    if (1000-a-b == c && a < b)
    {
        cout << a << " " << b << " " << c << "\n";
    }
}

int main()
{
    for (int i = 1; i < 1000; i++)
    {
        for (int j = 1; j < 1000; j++)
        {
            triple(i, j);
        }
    }

    return 0;
}
