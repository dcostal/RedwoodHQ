using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using OpenQA.Selenium; 


namespace F4
{
    class Generate_unique_Part_Number
    {
        public string Part_No(Dictionary<string, object> Params)
        {
             Random number = new Random();
             int random_number = number.Next(10000);
            
             String part_no = "PN101"+random_number;
             Thread.Sleep(1000);
             
             SendKeys.SendWait(part_no);
             Thread.Sleep(3000);
             Console.WriteLine(part_no);
            
               
             return(part_no);
        }
    }
}