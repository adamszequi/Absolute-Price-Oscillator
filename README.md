# Absolute-Price-Oscillator

The absolute price oscillator is a class of indicators that
builds on top of moving averages of prices to capture specific short-term deviations in
prices.

The absolute price oscillator is computed by finding the difference between a fast
exponential moving average and a slow exponential moving average. Intuitively, it is
trying to measure how far the more reactive EMA is deviating from the more
stable EMA. A large difference is usually interpreted as one of two things:
instrument prices are starting to trend or break out, or instrument prices are far away from
their equilibrium prices, in other words, overbought or oversold:

This is an implementation of the absolute price oscillator, with the faster EMA using a period of 10
days and a slower EMA using a period of 40 days, and default smoothing factors being 2/11
and 2/41, respectively, for the two EMAs.
