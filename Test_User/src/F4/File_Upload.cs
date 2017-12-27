using System;
using OpenQA.Selenium.Chrome;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using OpenQA.Selenium; 

namespace F4
{
    class File_Upload{
        public void run(Dictionary<string, object> Params)
        {
                    
             IWebDriver driver = new ChromeDriver();
             String baseURL = "http://10.20.5.181:3000/";
             
             //login code
             driver.Navigate().GoToUrl(baseURL + "login");
             Thread.Sleep(2000);
            /*
             driver.FindElement(By.Name("username")).Click();            
             driver.FindElement(By.Name("username")).SendKeys("admin");
            
             //Entering the Password
             driver.FindElement(By.Name("password")).Click();
             driver.FindElement(By.Name("password")).SendKeys("Password.1");
             Thread.Sleep(1500);

             //Clicking on Login Button
             driver.FindElement(By.XPath("/html/body/my-app/block-ui/div[2]/div[2]/main/login/div/div/form/section[3]/button")).Click();
            Thread.Sleep(2000);
             */
            Console.WriteLine("TEST");
            
        }
    }
}