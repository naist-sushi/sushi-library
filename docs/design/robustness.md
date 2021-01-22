## Robustness Diagram for List Books

```plantuml
@startuml
title Robustness(List Books)
actor User

package SushiLibrary{
    boundary ChoosePage
    boundary BookListPage

    control "Listup Books" as ListB
    control "Check the User" as CheckUser

    entity Book
    entity UserInfo

}

User --> ChoosePage
User <-- BookListPage

ChoosePage --> CheckUser

CheckUser --> ListB : If check is ok
CheckUser -- UserInfo

ListB -- Book
ListB -up-> BookListPage

@enduml
```
Basic Cource: The user access to the "ChoosePage". And "Check the User" checks if user is logginned or not. "Listup Books" read existing "Book" model. Finally "BookListPage" shows books information to the user.
Alternative Couse: If the user is not loggined SushiLibrary back to "ChoosePage".

## Robustness Diagram for Register Books
```plantuml
@startuml
title Robustness(Register Books)
actor User

package SushiLibrary{
    boundary ChoosePage
    
    boundary BookRegistrationPage

    control "Register Book" as RegB
    control "Check the User" as CheckUser

    entity Book
    entity UserInfo

}

User --> ChoosePage

ChoosePage --> CheckUser
CheckUser -- UserInfo
CheckUser --> BookRegistrationPage : If check is ok
RegB -- Book
RegB <-up- BookRegistrationPage
RegB --> ChoosePage

@enduml
```
Basic Cource: The user access to the "ChoosePage". And "Check the User" checks if user is logginned or not. After that SushiLibrary shows "BookRegistrationPage" and the user input forms. Finally "Register Book" make new Book model and register and back to "ChoosePage".
Alternative Couse: If the user is not loggined SushiLibrary back to "ChoosePage".
