/* Euler's Project problem #4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.*/

#include <QCoreApplication>
#include <QMap>
#include <QDebug>
#include <QString>

bool isPrime(int i)
    //returns true if i is a prime number
{
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

void findPrimeFactor(QMap<int, int> & primes, QMap<int, int> & factors, int & n)
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

int makePalin(int n)
//Takes the number n and turns it into a palindrome
//by reversing the digits and adding them at the end (RHS)
{
 //Try #1
    QString tempString1 = QString::number(n);
    qDebug() << "tempString1" << tempString1;
    QString tempString2;
    int len = tempString1.length();
    qDebug() << "len: " << len;
    for (int i = 0; i < len; i++)
    {
        tempString2[len - i] = tempString1[i];
        //qDebug() << "tempString2" << tempString2;
    }
    tempString2 = tempString2.simplified();

    qDebug() << "tempString2" << tempString2;


/*    for (int i = len; i < 2* len; i++)
    {
        tempString1[i] = tempString2[i];
    }
*/
    tempString1 = tempString1.append(tempString2);
    qDebug() << "tempString1" << tempString1;
    return tempString1.toInt();

/* //Try #2
    int i2 = 0;
    for (int i = 0; i < ?; i++)
    {

    }
*/
}

bool isPalindrome(int n)
//returns true if n is a palindrome
{
    QString s = QString::number(n);
    for (int i = 0; i < s.length()/2; i++)
        if (s[i]!=s[s.length()-1-i])
        {
            return false;
        }
    return true;
}



bool isInRange(int u, int l, int n)
//returns true if n is between upper and lower, both exclusive
{
    return n<u && n>l;
}


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
//Test makePalin function
//    int i1 = 12, i2 = 123, i3 = 1234;
//    qDebug() << makePalin(i1);
//    qDebug() << makePalin(i2);
//    qDebug() << makePalin(i3);

//Test isPalindrome
//    int i = 123321;
//    qDebug() << i << " " << isPalindrome(i);
//    i = 901109;
//    qDebug() << i << " " << isPalindrome(i);
//    i = 123331;
//    qDebug() << i << " " << isPalindrome(i);
    int u = 1000, l = 900; //Upper and lower limits for tests
    for (int i = l; i < u; i++)
    {
        for (int j = l; j < u; j++)
        {
            if (isPalindrome(i*j))
            {
                qDebug() << i << " * " << j << " = " << i*j;
            }
        }
        //l++;
    }

//build a list of the first few prime numbers
//    QMap<int, int> primes;
//    primes[0] = 1;
//    primes[1] = 2;
//    int index = 2;
//    qDebug() << "Calculating prime numbers...";
//    for (int i = 3; i < 1000; i+=2)
//    {
//        //qDebug() << "i: " << i << " " << isPrime(i);
//        if (isPrime(i))
//        {
//            primes[index] = i;
//            index++;
//        }
//    }

//    qDebug() << "\t...Done";

    //Algorithm steps
    //loop through:
    //  starting at the highest number (999), find the prime factors
    //  multiply the prime factors together in such a way that they make two 3-digit numbers
    //  if two 3-digit numbers are found, return the two three digit numbers
    //  If it is not possible to get two 3-digit numbers, repeat the loop
//    int halfPalin = 999; //represents half of the palindrome
//    int product;
//    while (halfPalin > 900)
//    {
//        product = makePalin(halfPalin);

//        //find the prime factors for a given number
//        qDebug() << "Calculating the factors...";
//        QMap<int, int> facts; //holds the prime factors
//        QMap<int, int> finalFactors; //holds the final (multiplied factors)
//        findPrimeFactor(primes, facts, product);
//        qDebug() << "\t...Done";

//        //print out the prime factors
//        qDebug() << "The factors are:";
//        for (int i = 0; i < facts.size(); i++)
//        {
//            qDebug() << "i: " << i << " factor: " << facts[i];
//        }



//        int size = facts.size();
//        int u = 1000, l = 99; //Upper and lower limits for tests
//        int k = 0;
//        //test for factors that are already in the correct range
//        for (int i = 0; i < size; i++)
//        {
//                if (isInRange(u, l, facts[i]))
//                {
//                    finalFactors[k] = facts[i];
//                    k++;
//                }
//        }
//        //test for factors that are not yet in the correct range
//        for (int i = 0; i < size; i++)
//        {
//            for (int j = 0; j < size; j++)
//            {
//                if (!isInRange(u, l, facts[i]))
//                {

//                }
//            }
//        }
//        halfPalin--;
//    }//end while
    return a.exec();
}
