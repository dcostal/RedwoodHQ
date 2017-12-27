using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Threading;

namespace Test_calculator
{
    class Open_calc
    {
        public void run(Dictionary<string, object> Params)
        {             
            	try
     			{
                    Process p = null;
                    if (p == null)
          			{
            			p = new Process();
            			p.StartInfo.FileName = "Calc.exe";
            			p.Start();
                        Thread.Sleep(2000);
                    	p.Close();
          			}
         			else
             			{
                			p.Close();
               	 			p.Dispose();
             			}
         		}
        	catch (Exception e)
            	{
                	Console.WriteLine("Excepton" + e.Message);
            	}           
        }
    }
}