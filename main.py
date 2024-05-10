#%%

from jinja2 import Template

serializer_class = config.module.serializers.BulletinInstanceFlatSerializer

serializer = serializer_class(
    bulletin, many=False, read_only=True, context={'request': None})
data = serializer.data

args = {
    "bulletin": data
}
args.update(self.template_data)
body_template = Template(self.body_template)
subject_template = Template(self.subject_template)
body = body_template.render(**args)
subject = subject_template.render(**args)
data = dict(body=body, subject=subject)

