# Generated by Django 4.2.6 on 2024-06-20 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("taskT", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("cat_id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name="task",
            name="catagory",
        ),
        migrations.AddField(
            model_name="task",
            name="due_at",
            field=models.DateField(default="2024-01-01"),
        ),
        migrations.AddField(
            model_name="task",
            name="user_id",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="taskT.user"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="cat_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="taskT.category",
            ),
        ),
    ]
