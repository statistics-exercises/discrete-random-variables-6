import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xvalues(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==100, "you have generated the wrong number of coordinates" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x coordinates in your plot are incorrect" )
  
  def test_yvalues(self) : 
      fighand=plt.gca()
      figdat = fighand.get_lines()[0].get_xydata()
      this_x, this_y = zip(*figdat)
      self.assertTrue( len(this_y)==100, "you have generated the wrong number of coordinates" )
      for i in range( len(this_x) ) :
          self.assertTrue( (this_y[i]-np.floor(this_y[i])) < 1e-7, "one or more of your random variables is not an integer" )
          self.assertTrue( this_y[i]>=0 and this_y[i] <= num, "one or more of your random variables falls outside the range it should be inside"  )
      mean = sum(this_y) / len(this_y) 
      bar = np.sqrt(num*prob*(1-prob)/100)*st.norm.ppf( (0.99 + 1) / 2 )
      self.assertTrue( np.fabs( mean - num*prob )<bar, "you appear to be sampling from the wrong distribution" )
  
