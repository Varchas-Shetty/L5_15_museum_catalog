# Reflection

1. **What did the analysis tools find?**
   They found style problems, unused code, and security risks such as unsafe SQL construction and a shell command.

2. **Which issue was most important to fix?**
   The SQL query was most important because user input was joined directly into the query. I changed it to use placeholders.

3. **How did the tools differ?**
   Pylint reported code quality and naming problems, Flake8 reported formatting and unused imports, and Bandit focused on security risks.

4. **What did you learn from this lab?**
   Static analysis can find problems before a program is used. I also learned to use parameterized SQL and avoid shell commands when they are not needed.
