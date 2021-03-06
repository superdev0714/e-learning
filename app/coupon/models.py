from django.db import models
from users.models import User
from django.utils import timezone
from config.common import STRIPE_SECRET_KEY
from django.contrib import messages
from django.db.models.signals import pre_delete
import json


class Coupon(models.Model):
    """
    This model stores the data of coupon.
    """
    name = models.CharField(max_length=150, help_text="coupon name", unique=True)
    percent = models.FloatField(help_text="coupon price")
    active = models.BooleanField(default=False,help_text="Active status of current coupon")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the Coupons.
        """

        return self.name

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    def save(self, *args, **kwargs):
        """
        Overrides default save to make sure:
        """

        # create a strip COUPON.
        import stripe
        from django.core.exceptions import ObjectDoesNotExist

        stripe.api_key = STRIPE_SECRET_KEY
        try:
            coupon = stripe.Coupon.create(
                name=self.name,
                percent_off=self.percent,
                duration="forever",
                id = self.name
            )
            super(Coupon, self).save(*args, **kwargs)
        except Exception as e:
            from subscription.models import ActivityLog

            ActivityLog.objects.create(**{
                "event": "COUPON_ERROR",
                "date": timezone.now(),
                "description": e.__str__(),
            })
            raise ObjectDoesNotExist("Error in creating coupon: "+e.__str__())

def remove_books(sender, instance, **kwargs):
    import stripe
    stripe.api_key = STRIPE_SECRET_KEY
    name = instance.name
    stripe.Coupon.delete(
        name,
    )
pre_delete.connect(remove_books, sender=Coupon)



class UserCoupon(models.Model):
    """
    This model store the data for the applied coupon user.
    """
    from subscription.models import SubscriptionPlan

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the User Applied Coupon.
        """

        return self.user.get_name() + " has used the coupon: " + self.coupon.name


    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        verbose_name = "User Coupon"
        verbose_name_plural = "User Coupons"
