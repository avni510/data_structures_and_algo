### Statistics and Probability 

# Independence
For 2 random variables X and Y, if the outcome of Y is completely unrelated to the outcome of X, then X and Y are said to
be independent.

# Sample space
- The set of all possible outcomes for a random variable.
- Each point in the sample space has a corresponding probability
- The sample space with all the probabilities is called the distribution
- Example:
  - X is the number of heads observed in four flips of a coin. The sample space of X is {0, 1, 2, 3, 4}.
  - The probabilities are given by a binomial distribution
    * 0 => 1/16
    * 1 => 1/4
    * 2 => 3/8
    * 3 => 1/4
    * 4 => 1/16

# Cummulative Distribution Function
- the probabiility of observing a value no larger than X. 
- Example:
  - I toss a coin twice. X be the number of heads observed. 
    * Fx(X) = P(X <= x) 
    * Sample space: {0, 1, 2}
      * 0 => 1/4
      * 1 => 1/2
      * 2 => 1/4
    * Fx(X)
      * 0 => for X < 0
      * 1/4 => for 0 <= X < 1
      * 3/4 => for 1 <= X < 2
      * 1 => for X <= 2

# Probablity Density Function
- the probability of observing a value of X between a and b is seql to the area
under the curve between a and b.
- normal distribution for pdf is the bell curve

# Types of Disributions
  * Discrete 
    - Definition: Discrete number of values. Coin tosses and counts of events. Ex: a binomial distribution can take on 2 values HT
    - Types:
      - Bernoulli
        * Success: denoted by 1, with probability p        
        * Failure: denoted by 0, with probability 1 - p
        * Ex: yes/no question
      - Binomial
        * An experiment with two possible outcomes (either a success or failure). 
        * Experiment is repeated many times. 
        * The reptitions are independent of each other. 
        * The total number of experiments where the outcome turns out to be a success is a RV with a binomial distribution
        * Can be seen as the number of successes of a Bernoulli trial.  
      - Poisson
        * Related to an exponential distribution
        * An event occurs several times within a given unit of time. 
        * When the total number occurences of the event are unknown 
      - Geometric 
        * the probability distribution of the number of failures we get by repeating a Bernoulli experiment, before the first success is obtained
        * We repeat the experiment until we get the first success. Then we count the number X of failures that we faced prior to recording a success
  * Continuous
    - Definition: Can assume infinite # of values 

# Right skewed vs. Left skewed
  * Right skewed -> long right tail
  * Left skewed -> long left tail

# Variance and Standard deviation
  * Variance
    - measures dispersion around its mean
    - σ ^ 2
  * Standard deviation -> square root of variance 
    - σ

# Expected Value / Mean
  * Expected Value of Random Variable X
    - is the weighted average of the values X can take on, where each possible value is weighted by its respective probability 
  * Mean
    - The average of the data set. Add all the values divide by the number of values
  * Difference between the two
    - When N is very large the average converges to the expected value (since all values will converge to the actually probability)

# Covariance and Correlation
  * Both measure relationship and dependency between variables
  * Covariance
    - Indicates the direction of the linear relationship between variables
    - how 2 variables are related
  * Correlation
    - a function of covariance
    - is the covariance normalized
    - correlation is standardized (always between -1 to 1)
    - measure both strength and direction of two variables 

# Law of Large numbers
  - As the number of trials increases the expected value of the sample converges to the expected value of the population (the true expected value)

# Central Limit Theorem
  - The distribution of the sample mean as when we increase the sample size
  - If n (sample size) is large enough the standard normal distribution is a good approximation of the distribution
    of the standardized sample mean

# Sampling Distribution/ Variation
  - Sampling Distribution/ Variation
    * The probability distribution of an estimator (sample mean or sample variance) over all possible outcomes
    * Ex: You conduct an experiment and calculate the sample mean. You continue to repeat this. The sampling distribution of the mean is if you plotted all your sample means
    * The mean of this distribution: E[X bar] = μ
    * The variance of this distribution: V[X bar] = (σ ^ 2)/n
    * Based on the central limit theorem: the sampling distribution of the estimator is normal distributed 

# Hypothesis testing
  - Method to make statistical inferences
  - hypothesis about populations not samples

  - null hypothesis: things are working as expected (no difference)
  - alternative hypothesis: there is a difference 
  - Ex:
      Ho: μ = 10
      Ha: μ ≠ 10
  - Type I error (false positive):
    * occurs when we decide in favor of Ha when Ho is true
  - Type II error (false negative):
    * occurs when we decide in favor of Ho when Ha is true

# z-score/ t-score and p values
  - Given Ho is true how many standard deviations away is the observed value 
  
            p̂ - po
   z =  --------------
        sqrt(p̂(1 - po)/ n)

         X bar - μo
   t = --------------- 
        Sx (standard deviation of sample)
        --------
        sqrt(n)

   * given t/ z score you can calculate the p value
   * p value is the probability of finding the observed value given the Ho is true
   * Set some sort of alpha compare p value to alpha to reject/ accept null hypothesis

# Confidence Interval
  * p̂ = .54
  * What is the probability that p̂ = .54 is within 2 standard deviations of p (the true population proportion) (95% confidence)
  * calculate the Standard Error with a formula. Say it is .05
  * With 95% confidence between .44 and .64 lies the true population proportion

# Probability Axioms
  * For any event E, 0 <= P(E) <= 1
  * For any events E and F, if they are mutually exclusive (the intersection is an empty set). P(E U F) = P(E) + P(F)
  * P(null set) = 0

# Bayes Theorem
  * Conditional probability
  * Governs reversing the direction of conditional probabilities 
  * Based on prior knowledge of conditions that might be related to an event

              P(E) * P(F | E)
   P(E | F) = -------------- 
                  P(F)

# Random Variable
  * Uncertain, numerical quantity
  * Random Phenomenon

# Conditional Probability
  * How the effects of one random variable effects the value of the other random variable
  
              P(A and B)
   P(A | B) = ----------        
                P(B)
# Independence
  * P(X and Y) = P(X) * P(Y)
