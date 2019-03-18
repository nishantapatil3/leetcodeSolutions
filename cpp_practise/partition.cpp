#include <iostream>
#include <algorithm> //for partion algorithm
#include <vector> //for vector

using namespace std;

int main(){
    // Initializing vector
    vector<int> vect = {2,3,5,7,6,4,8,9,1,2};

    //check if vector is partitioned
    // using is_partitioned()
    is_partitioned(vect.begin(), vect.end(), [](int x)
    {
        return x%2 == 0;
    })?
    cout << "vector is partitioned":
    cout << "vector is not partitioned";
    cout << endl; 

    //partioning vector using partition()
    partition(vect.begin(), vect.end(), [](int x)
    {
        return x%2==0;
    });

    //check if vector is partitioned
    // using is_partitioned()
    is_partitioned(vect.begin(), vect.end(), [](int x)
    {
        return x%2 == 0;
    })?
    cout << "now, vector is partitioned":
    cout << "vector is still not partitioned after partitioning";
    cout << endl;

    // Displaying partitioned Vector
    cout << "The partitioned vector is: ";
    for (int &x : vect) cout << x << " ";

    cout << endl;
    return 0;
}