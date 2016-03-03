# Save Mikrotik usage

Scripts in this repo can be used to retrieve usage from a Mikrotik device.
The aim initially will be to pull usage on intervals using the web access accounting interface,
but in the future might be expanded to rather use other methods, as this method is constrained
by the pair threshold set on the Mikrotik device (which means we might miss usage if the threshold
is hit between poll periods).
