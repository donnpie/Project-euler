//Euler project problem #3
//Find the largest prime factor for 600851475143
#include <QCoreApplication>
#include <QtDebug>
#include <QMap>


bool isPrime(long long int i)
{
    //returns true if i is a prime number
    if (i%2==0)
    {
        return false;
    }
    for (int j = 3; j < i/2; j+=2)
    {
        if (i%j==0)
            return  false;
    }
    return true;
}


void findPrimeFactor(QMap<int, long long int> & primes, QMap<int, long long int> & factors, long long int & n)
//Finds the prime factors of a number
{
    int index = 0;
    for (int i = 0; i < primes.size(); i++)
    {
        if (n % primes[i] == 0)
        {
            factors[index] = primes[i];
            qDebug() << "factor " << index << " is " << factors[index];
            index++;
        }
    }
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    //Example:
    //qDebug() << 13195;
    //qDebug() << 5*7*13*29; //equals 13195
    //600,851,475,143: //need a long long int to store this number

    //build a list of the first few prime numbers
    QMap<int, long long int> map;
    map[0] = 1;
    map[1] = 2;
    int index = 2;
    qDebug() << "Calculating prime numbers...";
    for (int i = 3; i < 10000; i+=2)
    {
        //qDebug() << "i: " << i << " " << isPrime(i);
        if (isPrime(i))
        {
            map[index] = i;
            index++;
        }
    }

    qDebug() << "\t...Done";
//print out the results
/*
    for (int i = 0; i < map.size(); i++)
    {
        qDebug() << "i: " << i << " prime: " << map[i];
    }
*/


    //find the prime factors for a given number
    qDebug() << "Calculating the factors...";
    long long int number = 600851475143;
    QMap<int, long long int> facts;
    findPrimeFactor(map, facts, number);
    qDebug() << "\t...Done";
    //print out the prime factors
    qDebug() << "The factors are:";
    for (int i = 0; i < facts.size(); i++)
    {
        qDebug() << "i: " << i << " factor: " << facts[i];
    }

    qDebug() << "Test:";
    qDebug() << "Target number: " << number;
    long long int answer = 1;
    for (int i = 0; i < facts.size(); i++)
    {
        answer *= facts[i];
    }
    qDebug() << "The calculated answer is: " << answer;

    return a.exec();
}
