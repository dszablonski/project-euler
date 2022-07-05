#include <iostream>
#include <vector>

using namespace std;

vector<unsigned long long int> sequence;

int nextTerm(int begin)
{
    if(begin % 2 == 0)
    {
        return (int)begin/2;
    }
    if(begin % 2 != 0)
    {
        return begin*3 + 1;
    }

    return 0;
}

void collatzSequence(int beginningTerm, vector<unsigned long long int> &sequence)
{
    int next_term;
    sequence.push_back(beginningTerm);
    int current_term = beginningTerm;

    while(current_term != 1)
    {
        next_term = nextTerm(current_term);
        sequence.push_back(next_term);
        current_term = next_term;
    }
}

int main()
{
    unsigned long long int temp;
    unsigned long long int size = 1;

    for(int i = 100000; i < 1000000; i++)
    {
        cout << "ITERATION: " << i << endl;

        collatzSequence(i, sequence);
        unsigned long long int tempSize = sequence.size();


        if(tempSize > size)
        {
            size = tempSize;
        }
        sequence.clear();
    }
    
    cout << "BIGGEST SEQUENCE HAS A SIZE OF: " << size << " ELEMENTS" << endl;

    return 0;
}