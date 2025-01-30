class Employee {
  constructor(
    name,
    birth_date,
    present_address,
    permanent_address,
    contact,
    department,
    joining_date,
    degination,
    salary
  ) {
    this.name = name;
    this.birth_date = birth_date;
    this.present_address = present_address;
    this.permanent_address = permanent_address;
    this.contact = contact;
    this.department = department;
    this.joining_date = joining_date;
    this.degination = degination;
    this.salary = salary;
  }
}

const employees = [
  new Employee(
    "Rahul",
    2000,
    "Dhaka",
    "Dhaka",
    "1234567890",
    50000,
    "Sales",
    "2020-01-01",
    "Sales Manager"
  ),
  new Employee(
    "Nusrat",
    1999,
    "Chittagong",
    "Chittagong",
    "0987654321",
    60000,
    "Marketing",
    "2021-02-01",
    "Marketing Manager"
  ),
  new Employee(
    "Sohan",
    1998,
    "Sylhet",
    "Sylhet",
    "0123456789",
    70000,
    "IT",
    "2022-03-01",
    "IT Manager"
  ),
  new Employee(
    "Tahmina",
    1997,
    "Khulna",
    "Khulna",
    "9876543210",
    80000,
    "HR",
    "2023-04-01",
    "HR Manager"
  ),
  new Employee(
    "Rasel",
    1996,
    "Rajshahi",
    "Rajshahi",
    "5432167890",
    90000,
    "Finance",
    "2024-05-01",
    "Finance Manager"
  ),
  new Employee(
    "Jannat",
    1995,
    "Barisal",
    "Barisal",
    "8765432109",
    100000,
    "Operations",
    "2025-06-01",
    "Operations Manager"
  ),
  new Employee(
    "Riad",
    1994,
    "Mymensingh",
    "Mymensingh",
    "2109876543",
    110000,
    "Customer Support",
    "2026-07-01",
    "Customer Support Manager"
  ),
  new Employee(
    "Sadia",
    1993,
    "Dhaka",
    "Dhaka",
    "3210987654",
    120000,
    "Legal",
    "2027-08-01",
    "Legal Manager"
  ),
  new Employee(
    "Mahfuz",
    1992,
    "Chittagong",
    "Chittagong",
    "4321098765",
    130000,
    "Product Management",
    "2028-09-01",
    "Product Management Manager"
  ),
  new Employee(
    "Tasnim",
    1991,
    "Sylhet",
    "Sylhet",
    "5432109876",
    140000,
    "Quality Assurance",
    "2029-10-01",
    "Quality Assurance Manager"
  ),
  new Employee(
    "Rafiq",
    1990,
    "Khulna",
    "Khulna",
    "6543210987",
    150000,
    "Business Development",
    "2030-11-01",
    "Business Development Manager"
  ),
  new Employee(
    "Nahid",
    1989,
    "Rajshahi",
    "Rajshahi",
    "7654321098",
    160000,
    "Accounting",
    "2031-12-01",
    "Accounting Manager"
  ),
  new Employee(
    "Mithun",
    1988,
    "Barisal",
    "Barisal",
    "8765432109",
    170000,
    "Human Resources",
    "2032-01-01",
    "Human Resources Manager"
  ),
  new Employee(
    "Jui",
    1987,
    "Mymensingh",
    "Mymensingh",
    "9876543210",
    180000,
    "Marketing",
    "2033-02-01",
    "Marketing Manager"
  ),
  new Employee(
    "Rohan",
    1986,
    "Dhaka",
    "Dhaka",
    "1098765432",
    190000,
    "IT",
    "2034-03-01",
    "IT Manager"
  ),
  new Employee(
    "Tahsin",
    1985,
    "Chittagong",
    "Chittagong",
    "2109876543",
    200000,
    "Finance",
    "2035-04-01",
    "Finance Manager"
  ),
  new Employee(
    "Samiha",
    1984,
    "Sylhet",
    "Sylhet",
    "3210987654",
    210000,
    "Operations",
    "2036-05-01",
    "Operations Manager"
  ),
  new Employee(
    "Raihan",
    1983,
    "Khulna",
    "Khulna",
    "4321098765",
    220000,
    "Customer Support",
    "2037-06-01",
    "Customer Support Manager"
  ),
  new Employee(
    "Nafisa",
    1982,
    "Rajshahi",
    "Rajshahi",
    "5432109876",
    230000,
    "Legal",
    "2038-07-01",
    "Legal Manager"
  ),
  new Employee(
    "Tahmid",
    1981,
    "Barisal",
    "Barisal",
    "6543210987",
    240000,
    "Product Management",
    "2039-08-01",
    "Product Management Manager"
  ),
  new Employee(
    "Rakib",
    1980,
    "Mymensingh",
    "Mymensingh",
    "7654321098",
    250000,
    "Quality Assurance",
    "2040-09-01",
    "Quality Assurance Manager"
  ),
  new Employee(
    "Sadia",
    1979,
    "Dhaka",
    "Dhaka",
    "8765432109",
    260000,
    "Business Development",
    "2041-10-01",
    "Business Development Manager"
  ),
  new Employee(
    "Rajib",
    1978,
    "Chittagong",
    "Chittagong",
    "9876543210",
    270000,
    "Accounting",
    "2042-11-01",
    "Accounting Manager"
  ),
  new Employee(
    "Tasnim",
    1977,
    "Sylhet",
    "Sylhet",
    "1098765432",
    280000,
    "Human Resources",
    "2043-12-01",
    "Human Resources Manager"
  ),
  new Employee(
    "Mahfuz",
    1976,
    "Khulna",
    "Khulna",
    "2109876543",
    290000,
    "Marketing",
    "2044-01-01",
    "Marketing Manager"
  ),
  new Employee(
    "Nahid",
    1975,
    "Rajshahi",
    "Rajshahi",
    "3210987654",
    300000,
    "IT",
    "2045-02-01",
    "IT Manager"
  ),
  new Employee(
    "Mithun",
    1974,
    "Barisal",
    "Barisal",
    "4321098765",
    310000,
    "Finance",
    "2046-03-01",
    "Finance Manager"
  ),
  new Employee(
    "Jui",
    1973,
    "Mymensingh",
    "Mymensingh",
    "5432109876",
    320000,
    "Operations",
    "2047-04-01",
    "Operations Manager"
  ),
  new Employee(
    "Rohan",
    1972,
    "Dhaka",
    "Dhaka",
    "6543210987",
    330000,
    "Customer Support",
    "2048-05-01",
    "Customer Support Manager"
  ),
  new Employee(
    "Tahsin",
    1971,
    "Chittagong",
    "Chittagong",
    "7654321098",
    340000,
    "Legal",
    "2049-06-01",
    "Legal Manager"
  ),
];

function displayEmployees() {
  const tableBody = document.getElementById("employee-data");
  tableBody.innerHTML = "";

  employees.forEach((employee) => {
    const row = `
            <tr>
                <td>${employee.name}</td>
                <td>${employee.birth_date}</td>
                <td>${employee.present_address}</td>
                <td>${employee.permanent_address}</td>
                <td>${employee.contact}</td>
                <td>${employee.department}</td>
                <td>${employee.joining_date}</td>
                <td>${employee.degination}</td>
                <td>${employee.salary}</td>
            </tr>
        `;
    tableBody.innerHTML += row;
  });
}

document.getElementById("btn1").addEventListener("click", displayEmployees);
