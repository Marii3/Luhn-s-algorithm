Hans Luhn's algorithm. Checking the validity of bank cards.

A credit card can contain from 13 to 16 digits in its number.

The first digits of the card can be:

4 Visa
5 MasterCard
37 American Express cards
6 Discover cards

1) Double every second digit from right to left. If the result of doubling contains two digits, then add them
to get a single character number.
(that is, if, for example, the number 6, doubled gives 12, then the result should be 3). If the result of doubling is single-digit, then leave it there.
2) Add up all the results of doublings in step 1.

For example, if we have a card number: 4388576018402626

then in step two, we should get: 4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

3) Add up all the numbers in odd positions from right to left.
i.e.: 6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

4) Add the results from step 2 and from step 3. 37 + 38 = 75

5) If the amount received is a multiple of 10, then the card is valid, if not, then the number is fake.