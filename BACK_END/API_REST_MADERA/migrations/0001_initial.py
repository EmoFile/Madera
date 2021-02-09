# Generated by Django 3.1.5 on 2021-02-08 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Composant',
            fields=[
                ('id_composant', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gamme',
            fields=[
                ('id_gamme', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id_module', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CompteClient',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('id_erp', models.IntegerField(unique=True)),
                ('encrypted_password', models.CharField(max_length=60)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('compteclient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compteclient')),
                ('mail', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compteclient',),
        ),
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('compteclient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compteclient')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compteclient',),
        ),
        migrations.CreateModel(
            name='UserAdministration',
            fields=[
                ('compteclient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compteclient')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compteclient',),
        ),
        migrations.CreateModel(
            name='UserBE',
            fields=[
                ('compteclient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compteclient')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compteclient',),
        ),
        migrations.CreateModel(
            name='UserIT',
            fields=[
                ('compteclient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compteclient')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compteclient',),
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id_piece', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('modules', models.ManyToManyField(to='API_REST_MADERA.Module')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleComposant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('composant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API_REST_MADERA.composant')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API_REST_MADERA.module')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='composants',
            field=models.ManyToManyField(through='API_REST_MADERA.ModuleComposant', to='API_REST_MADERA.Composant'),
        ),
        migrations.AddField(
            model_name='module',
            name='gamme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_REST_MADERA.gamme'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id_ticket', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('statut', models.CharField(max_length=25)),
                ('demande', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('traitement', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_REST_MADERA.userit')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id_plan', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=60)),
                ('lien_pdf', models.CharField(max_length=100)),
                ('auteur', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_REST_MADERA.userbe')),
            ],
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id_devis', models.AutoField(primary_key=True, serialize=False)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nom_devis', models.CharField(max_length=60)),
                ('pieces', models.ManyToManyField(to='API_REST_MADERA.Piece')),
                ('plan', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_REST_MADERA.plan')),
                ('client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_REST_MADERA.client')),
                ('commercial', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API_REST_MADERA.commercial')),
            ],
        ),
    ]
