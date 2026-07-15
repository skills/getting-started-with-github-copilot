// package com.example.browsersetup;

// import org.openqa.selenium.By;
// import org.openqa.selenium.WebDriver;
// //import org.openqa.selenium.chrome.ChromeDriver;
// import org.testng.annotations.*;
// import io.github.bonigarcia.wdm.WebDriverManager;

// public class BaseClass {
//     WebDriver driver;

//     @BeforeTest
//     public  WebDriver openBrowser() {
//         WebDriverManager.chromedriver().setup();
//         driver.manage().window().maximize();
//         driver.manage().window().maximize();
//         driver.get("https://www.saucedemo.com/");
//         driver.findElement(By.id("user-name")).sendKeys("standard_user");
//         driver.findElement(By.id("password")).sendKeys("secret_sauce");
//         driver.findElement(By.id("login-button")).click();
// return (driver);
//     }
// }
