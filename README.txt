Hospital Roldan (sitio web administrativo hospitalario)
- Proyecto realizado individualmente por Trinidad Roldan.
- Cuenta con 2 aplicaciones y un proyecto base.
- La apliación doctors sirve para agregar los doctores que realizarían las operaciones, donde el superuser puede ir agregando nuevos doctores mediante un formulario que esta en la ULR /doctors/newdoctor o haciendo click en botón crear de la sección de Doctores donde hay una lista de todos ellos.
- En doctors hay un modelo con los campos name, speciality y birth_date.
- En la URL list-doctors/ hay un buscador que filtra los nombres de los doctores.
- En la aplicación surgeries se pueden ver las cirugías que se realizarían, y también las categorías en las cuales estas se separan, esto se ve en los dos modelos que tiene esta app, que son Surgeries y Category.
- En el modelo Category se agregan los datos por la URL, y tiene solo un campo que es name
- El modelo Surgeries funciona igual que el modelo Doctors, con los campos organ, price y legal_age.