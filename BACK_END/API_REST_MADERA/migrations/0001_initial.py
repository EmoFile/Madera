# Generated by Django 3.1.5 on 2021-02-08 12:31

import API_REST_MADERA.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='Compte',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('id_erp', models.IntegerField(null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', API_REST_MADERA.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('compte_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compte')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compte',),
            managers=[
                ('objects', API_REST_MADERA.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('compte_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compte')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compte',),
            managers=[
                ('objects', API_REST_MADERA.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAdministration',
            fields=[
                ('compte_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compte')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compte',),
            managers=[
                ('objects', API_REST_MADERA.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserBE',
            fields=[
                ('compte_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compte')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compte',),
            managers=[
                ('objects', API_REST_MADERA.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserIT',
            fields=[
                ('compte_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_REST_MADERA.compte')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('API_REST_MADERA.compte',),
            managers=[
                ('objects', API_REST_MADERA.models.AccountManager()),
            ],
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
                ('etat', models.CharField(choices=[('En attente', 'Enattente'), ('Accepté', 'Accepte'), ('Refusé', 'Refuse')], default='En attente', max_length=20)),
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
