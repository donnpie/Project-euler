//Euler project problem #5
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include <QCoreApplication>
#include <QtDebug>
#include <math.h>

struct primeList
//Container for counting the number occurences of prime numbers
{
    int prime; //holds the prime number
    int count; //counts the maximum number of times a prime number appears
};

long long int factorial(long long int n)
//returns the factorial of n
{
    if (n<1)
    {
        return 0;
    }
    if (n == 1)
        return 1;
    else {
        return n * factorial(n-1);
    }
}

bool isPrime(int i)
//returns true if i is a prime number
{
    if (i == 1 || i == 2) return true;
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

void makePrimeList(QMap<int, primeList> & pList, int n)
//Creates a list of the first n prime numbers, index starts at 1
{
    int i = 1, j = 1; //i counts the iterations, j counts the prime numbers
    while (j <= n)
    {
        if (isPrime(i))
        {
            pList[j].prime = i;
            pList[j].count = 0;
            j++;
        }
        i++;
    }
}

int findPrime(QMap<int, primeList> & pList, int prime)
//finds prime in pList and returns the index
{
    for (int i = 0; i < pList.size(); i++)
    {
        if (pList[i].prime == prime)
        {
            return i;
        }
    }
    return 0; //If prime is not found, returns 0
}

void resetPrimeCount(QMap<int, primeList> & pList)
//Resets all the counts back to zero
{
    //qDebug() << "Resetting prime counts...";
    for (int i = 0; i < pList.size(); i++)
    {
        pList[i].count = 0;
    }
    //qDebug() << "...Done";
}


bool countPrimes(QMap<int, primeList> & pListOne, int n)
//Breaks n up into its prime factors and counts how many times each prime factor occurs
{
    //If the count of a prime factor is greater than the current value in pList, the count value in pList is overwritten
    //the pList here only counts the prime number occurences for this number
    const int START_COUNT = 2;
    if (isPrime(n))
    {
        //qDebug() << "Number is prime";
        int key = findPrime(pListOne, n);
        if (pListOne[key].count == 0)
        {
            pListOne[key].count = 1;
            return true;
        }
    }
    else
    {//Number is not prime
        //qDebug() << "Number is not prime";
        int num = n; //numerator
        int den = pListOne[START_COUNT].prime; //denominator
        int rem = num%den; //remainder
        int q = num/den; //quotient
        int count = pListOne.size();
        int i = START_COUNT; //index
        bool isDone = false;
        while (!isDone)
        {
            //qDebug() << "While clause started";
            if (q > 1 && rem == 0) //number is a factor of the denominator
            {
                //qDebug() << "\tNumber is a factor of the denominator";
                //qDebug() << "\t\tValues as found:";
                //qDebug() << "\t\t\ti: " << i;
                //qDebug() << "\t\t\tNumerator: " << num;
                //qDebug() << "\t\t\tDenominator: " << den;
                //qDebug() << "\t\t\tQuotient: " << q;
                //qDebug() << "\t\t\tRemainder: " << rem;
                pListOne[i].count++; //count the prime number
                num = q; //quotient becomes the new number
                i = START_COUNT; //reset the denominator
                den = pListOne[i].prime;
                q = num/den; //calculate the new quotient
                rem = num%den; //calculate the new remainder
                //qDebug() << "\t\tValues as left:";
                //qDebug() << "\t\t\ti: " << i;
                //qDebug() << "\t\t\tNumerator: " << num;
                //qDebug() << "\t\t\tDenominator: " << den;
                //qDebug() << "\t\t\tQuotient: " << q;
                //qDebug() << "\t\t\tRemainder: " << rem;
                //isDone = true; //debug code
            }
            else if (rem != 0) //number is not a factor of the denominator
            {
                //number stays the same, so num does not change
                //qDebug() << "\tNumber is not a factor of the denominator";
                i++; //go to the next denominator
                den = pListOne[i].prime;
                q = num/den; //calculate the new quotient
                rem = num%den; //calculate the new remainder

            }
            else if (q == 1 && rem == 0) //number is same as denominator
            {
                //qDebug() << "\tNumber is same as denominator********************************************************";
                pListOne[i].count++; //count the prime number
                isDone = true;
                return true;
            }
            if (i >= count)
            {
                //qDebug() << "Could not count primes";
                return false;
            }
        }
    }
    return false;
}

void countPrimes(const QMap<int, primeList> & pListOne, QMap<int, primeList> & pListAll)
//Compares the counts in pListOne to those in pListAll and transfers the count from one to all if one.count > all.count
{
    for (int i = 0; i < pListOne.size(); i++)
    {
        if (pListOne[i].count > pListAll[i].count)
        {
            pListAll[i].count = pListOne[i].count;
        }
    }
}

int lcm(QMap<int, primeList> & pListOne, QMap<int, primeList> & pListAll, const QMap<int, int> & numList)
//Returns the lowest common multiple of a series of numbers in listNum
{
    qDebug() << "Calculating the LCM...";
    for (int i = 1; i <= numList.size(); i++)
    {
        //qDebug() << "\ti: " << i << "numList[i]: " << numList[i];
        countPrimes(pListOne, numList[i]);
        countPrimes(pListOne, pListAll);
        resetPrimeCount(pListOne);
    }
    qDebug() << "...Done";
    int sum = 1;
    int count = pListAll.size();
    qDebug() << "Multiplying prime numbers...";
    //qDebug() << "pListAll.size(): " << pListAll.size();
    for (int i = 1; i <= count; i++)
    {
        //qDebug() << "\ti: " << i << "pListAll[i].prime: " << pListAll[i].prime << "pListAll[i].count: " << pListAll[i].count;
        if (pListAll[i].count > 0)
        {
            sum *= pow(pListAll[i].prime, pListAll[i].count);
            qDebug() << "\tSum: " << sum;
        }
        //qDebug() << "pListAll.size(): " << pListAll.size();
    }
    qDebug() << "...Done";
    return sum;
}


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    const int NUM_LIST_SIZE = 20;
    const int PRIME_LIST_SIZE = 9;

    //Check the factorial function for overflow
//    for (int i = 1; i <= 20; i++)
//    {
//        qDebug() << factorial(static_cast<long long int>(i));
//    }

//Test the isPrime function
//    for (int i = 1; i <= 30; i++)
//    {
//        qDebug() << i << " " << isPrime(i);
//    }

//Test the makePrimeList function
    QMap<int, primeList> pListAll;
    QMap<int, primeList> pListOne;
    makePrimeList(pListAll, PRIME_LIST_SIZE);
    makePrimeList(pListOne, PRIME_LIST_SIZE);
    //qDebug() << "The list of primes is:";
//    for (int i = 1; i <= PRIME_LIST_SIZE; i++)
//    {
//        qDebug() << i << " " << pListOne[i].prime << " " << pListOne[i].count;
//    }

//Test the findPrime function
//    for (int i = 1; i <= 200; i++)
//    {
//        if (isPrime(i))
//        {

//        qDebug() << "Key: " << findPrime(pList, i) << " Prime: " << i;
//        }
//    }

//Test the countPrimes function
//    for (int i = 1; i <= 10; i++)
//    {
//        //int i = 18;
//        //qDebug() << i;
//        countPrimes(pListOne, i);
//        countPrimes(pListOne, pListAll);
//        resetPrimeCount(pListOne);
//        //qDebug() << "Key: " << findPrime(pListOne, i) << " Prime: " << i << "Count: " << pListOne[findPrime(pListOne, i)].count;
//    }

//    for (int j = 1; j <= 5; j++)
//    {
//        qDebug() << "Key: "  << j << " Prime: " << pListAll[j].prime << " Count: " << pListAll[j].count;
//    }

    QMap<int, int> numList;
    qDebug() << "Building the numList...";
    for (int i = 1; i <= NUM_LIST_SIZE; i++)
    {
        numList[i] = i;
    }
    qDebug() << "...Done";

//get lcm
    qDebug() << "LCM: " << lcm(pListOne, pListAll, numList);
    //lcm(pListOne, pListAll, numList);

/*
    long long int number = 15; //This is the number of terms that are evenly divisible
    long long int fact = factorial(number); //use the factorial as a proxy for smalles common denominator
    qDebug() << "Factorial: " << fact;

    //multiply each term by the factorial
    long long int sum = 0;
    for (int i = 1; i <= number; i++)
    {
        sum += fact/static_cast<long long int>(i);
        qDebug() << "sum: " << sum;
    }
*/
/*
    double sum = 0;
    for (int i = 1; i <= number; i++)
    {
        sum += 1.0/static_cast<double>(i);
        qDebug() << "sum: " << sum;
    }
    //sum = 1/sum;
    qDebug() << "sum reciprocal: " << sum;
*/


/*    //Find the number
    int range = 20000;
    int answer = 0;
    bool test;
    long long int remainder = fact;
    for (int i = 1; i <= range; i++)
    {
        test = ((static_cast<long long int>(i)*fact)%sum == 0);
        if (static_cast<long long int>(i)*fact%sum < remainder)
        {
            remainder = static_cast<long long int>(i)*fact%sum;
        }
        qDebug() << "Remainder: " << remainder;
        qDebug() << "i: " << i << "test: " << test;
        if (test)
        {
            answer = (static_cast<long long int>(i)*fact)/sum;
            qDebug() << "*************************************************************************";
            break;
        }

    }
    qDebug() << "answer: " << answer;
*/

    return a.exec();
}
