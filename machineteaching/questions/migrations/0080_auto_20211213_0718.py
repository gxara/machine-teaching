# Generated by Django 2.2.5 on 2021-12-13 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0079_auto_20210913_2324'),
    ]

    operations = [
        migrations.RunSQL("""drop view if exists questions_outcome_summary""", ""),
        migrations.RunSQL("""drop view if exists questions_userlogview""", ""),
		migrations.RunSQL('''CREATE VIEW questions_outcome_summary
AS SELECT distinct_query.user_id,
    distinct_query.problem_id,
    sum(distinct_query.outcome) AS outcome,
        CASE
            WHEN sum(distinct_query.outcome) >= 4 THEN 'P'
            WHEN sum(distinct_query.outcome) >= 2 THEN 'F'
            WHEN sum(distinct_query.outcome) = 1 THEN 'S'
            ELSE NULL
        END AS final_outcome,
    distinct_query.user_class_id
   FROM ( SELECT questions_userlog.user_id,
            questions_userlog.problem_id,
            questions_userlog.user_class_id,
                CASE
                    WHEN questions_userlog.outcome = 'P' THEN 4
                    WHEN questions_userlog.outcome = 'F' THEN 2
                    WHEN questions_userlog.outcome = 'S' THEN 1
                    ELSE NULL
                END AS outcome
           FROM questions_userlog,
            questions_onlineclass
          WHERE questions_userlog.user_class_id = questions_onlineclass.id AND questions_userlog."timestamp" >= questions_onlineclass.start_date
          GROUP BY questions_userlog.user_id, questions_userlog.problem_id, questions_userlog.outcome, questions_userlog.user_class_id
          ORDER BY questions_userlog.user_id, questions_userlog.problem_id) distinct_query
  GROUP BY distinct_query.user_id, distinct_query.problem_id, distinct_query.user_class_id
  ORDER BY distinct_query.user_id, distinct_query.problem_id;''',
	"drop view questions_outcome_summary"),
        migrations.RunSQL('''
CREATE VIEW questions_userlogview
AS SELECT grouped_query.user_id,
    grouped_query.problem_id,
    grouped_query.outcome,
    grouped_query.final_outcome,
    grouped_query."timestamp",
    questions_userlog.seconds_in_page,
    questions_userlog.seconds_in_code,
    grouped_query.user_class_id
   FROM ( SELECT questions_outcome_summary.user_id,
            questions_outcome_summary.problem_id,
            questions_outcome_summary.outcome,
            questions_outcome_summary.final_outcome,
            min(questions_userlog_1."timestamp") AS "timestamp",
            questions_outcome_summary.user_class_id
           FROM questions_outcome_summary,
            questions_userlog questions_userlog_1,
            questions_onlineclass
          WHERE questions_userlog_1.user_id = questions_outcome_summary.user_id AND questions_userlog_1.problem_id = questions_outcome_summary.problem_id AND questions_userlog_1.outcome = questions_outcome_summary.final_outcome AND questions_outcome_summary.user_class_id = questions_onlineclass.id AND questions_outcome_summary.user_class_id = questions_userlog_1.user_class_id AND questions_userlog_1."timestamp" >= questions_onlineclass.start_date
          GROUP BY questions_outcome_summary.user_id, questions_outcome_summary.problem_id, questions_outcome_summary.outcome, questions_outcome_summary.final_outcome, questions_outcome_summary.user_class_id) grouped_query,
    questions_userlog
  WHERE grouped_query.user_id = questions_userlog.user_id AND grouped_query."timestamp" = questions_userlog."timestamp"''',
        "drop view questions_userlogview"),
    ]