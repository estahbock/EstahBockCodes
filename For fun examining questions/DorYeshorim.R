dor_yeshorim <- function(Npeople, Nchildren, init_freq, Ngen) 
{
  a = numeric(Ngen)
  b = numeric(Ngen)
  z = numeric(Ngen)
  # Used by Dor Yeshorim:
  a[1] = init_freq*Npeople # # of carriers in first generation (Dor Yeshorim)
  z[1] = (1 - init_freq)*Npeople # # of noncarriers in first generation (Dor Yeshorim)
  b[1] = init_freq

  # Loop for generation(s) with Dor Yeshorim:
  
  for (i in 2:Ngen)
  {
    (a[i-1]*Nchildren/2) -> a[i] # half of children from carriers are carriers
    ((z[i-1]-a[i-1])*Nchildren/2) + (a[i-1]*Nchildren/2) -> z[i] 
    # people not married to carriers double up and all children
    # not carriers. Those married to carriers have half of the children 
    # as noncarriers
    (a[i]/(a[i]+z[i])) -> b[i]
  }
 
  b
  
}

nature <- function(Npeople, Nchildren, init_freq, Ngen) 
{
  x = numeric(Ngen)
  y = numeric(Ngen)
  e = numeric(Ngen)
  # Used by Nature:
  x[1] = init_freq*Npeople # # of carriers in first generation
  y[1] = (1 - init_freq)*Npeople # # of noncarriers in first generation
  e[1] = init_freq
  
  # Loop for generation(s) with Nature:
  
  for (i in 2:Ngen)
  {
    (e[i-1]*x[i-1]/2) -> TScouples
    (TScouples*Nchildren/2)+((x[i-1]-(TScouples*2))*Nchildren/2) -> x[i]
    ((y[i-1]-(x[i-1]-(TScouples*2)))*Nchildren/2)+
      ((x[i-1]-(TScouples*2))*Nchildren/2)+
      (TScouples*Nchildren/4) -> y[i]
    (x[i]/(x[i]+y[i])) -> e[i]
  }
  
  e
  
}

dor_yeshorim(1000, 4, (1/27), 2)
nature(1000, 4, (1/27), 2)

dor_yeshorim(1000, 6, (1/27), 10)
nature(1000, 6, (1/27), 10)

dor_yeshorim(1000, 4, (1/27), 1000)
nature(1000, 4, (1/27), 1000)
