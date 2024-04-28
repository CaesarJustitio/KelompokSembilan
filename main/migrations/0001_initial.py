# Generated by Django 5.0.4 on 2024-04-28 10:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=100)),
                ('gender', models.IntegerField(choices=[(0, 'Female'), (1, 'Male')])),
                ('tempat_lahir', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField()),
                ('is_verified', models.BooleanField(default=False)),
                ('kota_asal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Konten',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=100)),
                ('tanggal_rilis', models.DateField()),
                ('tahun', models.IntegerField()),
                ('durasi', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('kontak', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paket',
            fields=[
                ('jenis', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PemilikHakCipta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rate_royalti', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NonPremium',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.akun')),
            ],
        ),
        migrations.CreateModel(
            name='Podcaster',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.akun')),
            ],
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.akun')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=100)),
                ('jumlah_lagu', models.IntegerField(default=0)),
                ('total_durasi', models.IntegerField(default=0)),
                ('id_label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.label')),
            ],
        ),
        migrations.AddField(
            model_name='label',
            name='id_pemilik_hak_cipta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pemilikhakcipta'),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email_akun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.akun')),
                ('id_pemilik_hak_cipta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pemilikhakcipta')),
            ],
        ),
        migrations.CreateModel(
            name='Songwriter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email_akun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.akun')),
                ('id_pemilik_hak_cipta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pemilikhakcipta')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp_dimulai', models.DateTimeField()),
                ('timestamp_berakhir', models.DateTimeField()),
                ('metode_bayar', models.CharField(max_length=50)),
                ('nominal', models.IntegerField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.akun')),
                ('jenis_paket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.paket')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id_konten', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.konten')),
                ('email_podcaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.podcaster')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id_episode', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=100)),
                ('deskripsi', models.CharField(max_length=500)),
                ('durasi', models.IntegerField()),
                ('tanggal_rilis', models.DateField()),
                ('id_konten_podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.podcast')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id_konten', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.konten')),
                ('total_play', models.IntegerField(default=0)),
                ('total_download', models.IntegerField(default=0)),
                ('id_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.album')),
                ('id_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('id_konten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.konten')),
            ],
            options={
                'unique_together': {('id_konten', 'genre')},
            },
        ),
        migrations.CreateModel(
            name='SongwriterWriteSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_songwriter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.songwriter')),
                ('id_song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.song')),
            ],
            options={
                'unique_together': {('id_songwriter', 'id_song')},
            },
        ),
    ]
