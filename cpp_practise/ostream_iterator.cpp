/*
cpp program to read a bunch of input from istream
print the sorted order of even integers only
*/

#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

int main(){
    //define vector to store output
    vector<int> v1;

    //define input stream
    istream_iterator<int> cin_it(cin);
    istream_iterator<int> eos;

    //define output stream 
    ostream_iterator<int> cout_it(cout, " ");

    //copy even integers to vector
    for_each(cin_it, eos, [&](int a){
        if (a%2==0){
            v1.push_back(a);
        }
    });

    //sort the vector
    sort(v1.begin(), v1.end());

    //copy elements from vector to output
    copy(v1.begin(), v1.end(), cout_it);

    return 0;
}