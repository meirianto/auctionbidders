# Final-Project

## Questions 
* What do we initialize the prior distributions to be? The paper mentions the parameters for the "real" distributions, but we're not sure how to initialize our first estimated parameters.
* How do we learn and update the parameters for the number of bidders? Each time we simulate the auction, we generate a new number of bidders. That estimation is drawn from an old distribution, so we don't know if we should use that to update g(m) or what to use instead.
* What is the maximun error accepted for convergence? 
* Can the bid value be negative? If so, what does it mean for it to be negative? If not, are we biasing the normal distribution?
