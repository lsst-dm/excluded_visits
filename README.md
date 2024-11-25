excluded_visits
=====

This repository contains lists of visits that are unprocessable or need to be excluded from processing to avoid contaminating output data products. Examples of images we want to exclude are visits where the telescope tracking failed, dome occultations, or bright lights contaminating large parts of the image. This should not include images where small portions of the image were affected by scattered light, satellites, airplanes, or other cases where much of the data is recoverable. This list does not need to include images that were not taken as "science" images; e.g. bad acquisition images do not need to be tracked.

Structure
----
This repository contains one directory for each camera, and one csv file for each tagged collection of raw images. Currently we are maintaining a `bad.ecsv` list for science visits to be excluded. The only two fields in the csv file are the exposure id (which is the same as the visit ID unless we are taking snap data) and a comment.

For example, the file looks like:

```
2024111800077, telescope slew during exposure 
2024111800078, telescope slew during exposure
```

The comment is only for convenience and it does not need to follow a strict form. 


Adding additional visits
----

1. Add the new visits to bad.ecsv. Keep the list sorted by exposure id.
2. Commit to a user branch and push.
3. Open a PR on GitHub.
4. Once the tests pass, you can merge. You *do not need a review*, and you do not need a Jira ticket.
