# Assignment Details
- Draw a database diagram for an online assessment platform. Highlight all relationships and keys. Feel free to use any database of your choice.
- Write a web crawler that is triggered by an API call to a web service. It takes 2 parameters:- root webpage to crawl, depth to which to crawl to. The web service returns a JSON with crawled links upto the depth. Design the API contract for maximum utility.

## Input for web crawler API
```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://anuragsingh.dev", "depth": 1}' http://localhost:5000/crawl
```

## Web Crawler API output (depth = 1)
Refer [output.json](./output.json) file for depth = 2 output for web crawler API
```
{
  "data": {
    "https://anuragsingh.dev": [
      "https://medium.com/@ashleymavericks",
      "https://youtube.com/@ashleymavericks",
      "https://stats.uptimerobot.com/wywn1IvQxB",
      "https://t.me/ashleymavericks",
      "https://linkedin.com/in/ashleymavericks/",
      "https://github.com/ashleymavericks",
      "https://dev.to/ashleymavericks",
      "https://twitter.com/ashleymavericks",
      "https://anuragsingh.dev/posts/index.xml",
      "https://leetcode.com/ashleymavericks"
    ]
  },
  "status": "success"
}
```

## Database ER diagram schema for Online Assessment Platform
```
erDiagram
    User {
        integer user_id (PK)
        varchar name
        varchar email
        varchar password
    }
    Assessment {
        integer assessment_id (PK)
        varchar name
        varchar description
    }
    Question {
        integer question_id (PK)
        varchar question_text
        integer assessment_id (FK) references Assessment(assessment_id)
    }
    Answer {
        integer answer_id (PK)
        varchar answer_text
        bool is_correct
        integer question_id (FK) references Question(question_id)
    }
    Result {
        integer result_id (PK)
        integer user_id (FK) references User(user_id)
        integer assessment_id (FK) references Assessment(assessment_id)
        integer score
        date date_taken
    }
```