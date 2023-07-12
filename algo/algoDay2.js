/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/
// First Method
const str1 = "object oriented programming";
const expected1 = "OOP";



function acronymString(string)
{
    var arr=string.split(" ");
    for(var i=0 ; i<arr.length;i++)
    {
 
        arr[i]= arr[i][0].toUpperCase()+arr[i].slice(1); 
    }

return arr.join(" ");

}
console.log(acronymString(str1))


// 2nd Method
function acronymString(string)

    for(var i=0 ; i<string.length();i++)
    {

        if(string[i] == " " )
    }

return arr.join(" ");

}
console.log(acronymString(str1))



// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

function acronymize(str) {}